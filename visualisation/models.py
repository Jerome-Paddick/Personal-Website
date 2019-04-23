from django.db import models
# Import models from other apps with / from app.models import modelname


class NetworkMapNodes(models.Model):
    group = models.IntegerField("Node ID",
                                unique=True)
    name = models.CharField("Node Name",
                            max_length=100)
    value = models.IntegerField("Size of Node",
                                default=1)

    # Metadata
    class Meta:
        ordering = ['-name']


class NetworkMapConnections(models.Model):
    source = models.ForeignKey(NetworkMapNodes,
                               verbose_name="Source Node ID",
                               related_name="source",
                               on_delete=models.CASCADE)
    target = models.ForeignKey(NetworkMapNodes,
                               verbose_name="Target Node ID",
                               related_name="target",
                               on_delete=models.CASCADE)
    value = models.IntegerField("Connection Strength",
                                default=1)

    # Metadata
    class Meta:
        ordering = ['-source']


class CountryMap(models.Model):
    country = models.CharField("Country Code",
                               max_length=3)
    value = models.IntegerField("Colour Intensity",
                                default=0)
    # @classmethod
    # def ingest_countries(self, input_country, value):
    #     if input_country.length() == 3:
    #         CountryMap.create(country=input_country,
    #                           value=value)


class NeuralNetTestData(models.Model):
    name = models.CharField(max_length=20)
    Input1 = models.IntegerField()
    Input2 = models.IntegerField()
    target = models.IntegerField()