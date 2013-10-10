from feincms.module.page.models import Page


Page.register_templates(
    {
        'key': 'main',
        'title': 'Main',
        'path': 'base.html',
        'regions': (
            ('main', 'Main column'),
        ),
    },
)
