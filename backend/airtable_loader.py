import sys
import os
import django
import argparse

from django.db import transaction
from airtable import Airtable

sys.path.append('meta')
os.environ['DJANGO_SETTINGS_MODULE'] = 'meta.settings'
django.setup()


from psychotherapists.models import Psychotherapist


def main(base_key, api_key, table_name):
    airtable = Airtable(base_key, table_name, api_key=api_key)

    records = airtable.get_all()

    with transaction.atomic():
        alive_pks = []
        for record in records:
            try:
                obj = Psychotherapist.objects.get(
                    data__contains={'id': record['id']},
                )
                obj.data = record
                obj.save()
            except Psychotherapist.DoesNotExist:
                obj = Psychotherapist.objects.create(data=record)

            alive_pks.append(obj.pk)

        Psychotherapist.objects.exclude(pk__in=alive_pks).delete()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--basekey", "-b", help="Set base key")
    parser.add_argument("--apikey", "-a", help="Set API key")
    parser.add_argument("--tablename", "-t", help="Set table name key")

    args = parser.parse_args()

    main(args.basekey, args.apikey, args.tablename)
