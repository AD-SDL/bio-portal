import logging
from django.shortcuts import render

from globus_portal_framework.views.generic import SearchView

log = logging.getLogger(__name__)


class BIOSearchView(SearchView):
    """Custom BIO Search view automatically filters on the bio 'project'. This is old,
    based on the pilot project feature and will be going away eventually."""

    @property
    def filters(self):
        default_filters = self.get_index_info().get("default_filters", [])
        filters = [f for f in default_filters if f.get("values")]
        if not filters:
            log.warning(
                'Please add a value for "SEARCH_FILTERS.values" in your '
                "app config, or else the manifest.json will continue appearing "
                "as a search result!"
            )
        print(str(self.get_index_info()))
        return super().filters + filters


def example_view(request, index):
    """
    Example custom view for rendering custom things.

    Rendering any template off of base should be fine, for example:

    ```
    {% extends "globus-portal-framework/v2/base.html" %}

    {% block body %}

    <h1>Hello {{context}}</h1>

    {% endblock %}
    ```
    Please note the ALCF portal uses custom branding, and any changes rendered locally will
    change according to branding there. Double check any styling changes before deployment.
    """
    context = {"context": "world"}
    return render(request, "bio/globus-portal-framework/v2/example-view.html", context)
