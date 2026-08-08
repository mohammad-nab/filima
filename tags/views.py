from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAdminUser
from django.db.models import Q
from rest_framework.response import Response
from conf.pagination import CustomPagination


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination

    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser]

    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class LanguageStatusViewSet(viewsets.ModelViewSet):
    queryset = LanguageStatus.objects.all()
    serializer_class = LanguageStatusSerializer
    permission_classes = [IsAdminUser]

    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class YearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination

    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class BannerLocationViewSet(viewsets.ModelViewSet):
    queryset = BannerLocation.objects.all()
    serializer_class = BannerLocationSerializer
    permission_classes = [IsAdminUser]

    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class TargetAudienceViewSet(viewsets.ModelViewSet):
    queryset = TargetAudience.objects.all()
    serializer_class = TargetAudienceSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class InformTypeViewSet(viewsets.ModelViewSet):
    queryset = InformType.objects.all()
    serializer_class = InformTypeSerializer
    permission_classes = [IsAdminUser]

    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class AccountStatusViewSet(viewsets.ModelViewSet):
    queryset = AccountStatus.objects.all()
    serializer_class = AccountStatusSerializer
    permission_classes = [IsAdminUser]

    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class TagSearchApiView(APIView):
    permission_classes = [IsAdminUser]


    def get(self, request):
        query = request.query_params.get('tags', "").strip()
        tag_type = request.query_params.get('type', "all").strip()

        result = []

        if tag_type in ["all", "genre"]:
            genres = Genre.objects.filter(
                is_deleted=False,
                name__icontains=query
            )

            for genre in genres:
                result.append({
                    "type": "genre",
                    "uuid": genre.genre_uuid,
                    "name": genre.name,
                    "slug": genre.slug,
                })

        if tag_type in ["all", "actor"]:
            actors = Actor.objects.filter(
                is_deleted=False,
                full_name__icontains=query
            )

            for actor in actors:
                result.append({
                    "type": "actor",
                    "uuid": actor.actor_uuid,
                    "name": actor.full_name,
                    "slug": actor.slug
                })

        if tag_type in ["all", "country"]:
            countries = Country.objects.filter(
                is_deleted=False,
                name__icontains=query
            )

            for country in countries:
                result.append({
                    "type": "country",
                    "uuid": country.country_uuid,
                    "name": country.name,
                    "slug": country.slug,
                })

        if tag_type in ["all", "language_status"]:
            language_statuses = LanguageStatus.objects.filter(
                is_deleted=False,
                status__icontains=query
            )

            for language_status in language_statuses:
                result.append({
                    "type": "language_status",
                    "uuid": language_status.language_status_uuid,
                    "status": language_status.status,
                    "slug": language_status.slug,
                })

        if tag_type in ["all", "year"]:
            years = Year.objects.filter(
                is_deleted=False,
                year__icontains=query
            )

            for year in years:
                result.append({
                    "type": "year",
                    "uuid": year.year_uuid,
                    "year": year.year,
                    "slug": year.slug,
                })

        if tag_type in ["all", "banner_location"]:
            banner_locations = BannerLocation.objects.filter(
                Q(is_deleted=False),
                Q(banner_name__icontains=query) | Q(location__icontains=query) )

            for banner_location in banner_locations:
                result.append({
                    "type": "banner_location",
                    "uuid": banner_location.banner_location_uuid,
                    "location": f"{banner_location.banner_name} {banner_location.location}",
                    "slug": banner_location.slug,
                })

        if tag_type in ["all", "target_audience"]:
            target_audiences = TargetAudience.objects.filter(
                is_deleted=False,
                audience__icontains=query
            )

            for target_audience in target_audiences:
                result.append({
                    "type": "target_audience",
                    "uuid": target_audience.target_audience_uuid,
                    "audience": target_audience.audience,
                    "slug": target_audience.slug,
                })

        if tag_type in ["all", "inform_type"]:
            inform_types = InformType.objects.filter(
                is_deleted=False,
                type__icontains=query
            )

            for inform_type in inform_types:
                result.append({
                    "type": "inform_type",
                    "uuid": inform_type.inform_type_uuid,
                    "inform_type": inform_type.type,
                    "slug": inform_type.slug,
                })

        if tag_type in ["all", "account_status"]:
            account_statuses = AccountStatus.objects.filter(
                is_deleted=False,
                status__icontains=query
            )

            for account_status in account_statuses:
                result.append({
                    "type": "account_status",
                    "uuid": account_status.account_status_uuid,
                    "status": account_status.status,
                    "slug": account_status.slug,
                })

        return Response(result)