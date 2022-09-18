from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination as _LimitOffsetPagination


def get_paginated_response(pagination_class, serializer_class,
                           queryset, request, view, context={}):
    """

    :param pagination_class: pagination class
    :param serializer_class: serializer class
    :param queryset: QuerySet
    :param request: request object
    :param view:
    :return: Json Response
    """
    paginator = pagination_class()

    page = paginator.paginate_queryset(queryset, request, view=view)

    if page is not None:
        serializer = serializer_class(page, many=True, context=context)
        return paginator.get_paginated_response(serializer.data)

    serializer = serializer_class(queryset, many=True, context=context)

    return Response(data=serializer.data)


class LimitOffsetPagination(_LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

    def get_paginated_data(self, data):
        return OrderedDict([
            ('limit', self.limit),
            ('offset', self.offset),
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ])

    def get_paginated_response(self, data):
        """
        We redefine this method in order to return `limit` and `offset`.
        This is used by the frontend to construct the pagination itself.
        """
        return Response(OrderedDict([
            ('limit', self.limit),
            ('offset', self.offset),
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
