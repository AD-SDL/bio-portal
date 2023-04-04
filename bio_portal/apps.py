import os
from django.apps import AppConfig

from bio_portal import fields

APP_DIR = os.path.join(os.path.dirname(__file__))


class BIOIndexConfig(AppConfig):
    name = "bio_portal"

SEARCH_INDEXES = {
    "sdl-bio": {
        "uuid": "4e2884b0-e585-4913-8a33-4be155ebb06c",
        "name": "SDL BIO Index",
        "group": "dda56f31-53d1-11ed-bd8b-0db7472df7d6",
        "collection": "bb8d048a-2cad-4029-a9c7-671ec5d1f84d",
        "base_templates": "globus-portal-framework/v2/",
        "template_override_dir": "bio",
        "tabbed_project": False,
        "access": "private",
        "description": ("Self Driving Laboratories @ BIO"),
        "fields": [
            ("title", fields.title),
            "dc",
            "files",
            ("final_plates",fields.final_plates),
            ("all_files",fields.all_files),
            ("exp_type",fields.exp_type),
            ("result", fields.results),
            ("final_img", fields.final_img),
            ("target_color", fields.target_color),
            ("best_color", fields.best_color),
            ("real_plates", fields.real_plates),
            ("exp_plates", fields.exp_plates)
        ],
        "facets": [
            {
                "name": "Creator",
                "field_name": "dc.creators.creatorName",
            },
            {
                "name": "Dates",
                "field_name": "dc.dates.date",
                "type": "date_histogram",
                "date_interval": "day",
            },
              {
                  "name": "Experiment Type",
                  "field_name": "title",
    
              }
        ],
        "facet_modifiers": [],
        "sort" : [
             {'field_name': 'dc.dates.date', 
                    'order': 'desc'
            }
        ],
        "default_filters": [
            {
                "type": "match_all",
                "field_name": "project_metadata.project-slug",
                "values": ['reports'],
            }
        ]
        
    }
}
