from django.db import models


class VisibleModel(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=256
    )
    is_visible = models.BooleanField(
        verbose_name='В зоне видимости',
        default=True,
        help_text='Снимите галочку, что бы убрать из поиска'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Mark(VisibleModel):
    producer_country_name = models.CharField(
        verbose_name='Страна производитель',
        max_length=256
    )

    class Meta:
        verbose_name = 'марка'
        verbose_name_plural = 'Марки'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_mark')
        ]


class Model(VisibleModel):
    mark = models.ForeignKey(
        Mark,
        verbose_name='Марка',
        related_name='mark',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'Модели'
        constraints = [
            models.UniqueConstraint(fields=['mark_id', 'name'], name='unique_model_mark')
        ]

    def mark_name(self):
        return self.mark.name

    mark_name.short_description = 'Марка'


class Part(VisibleModel):
    mark = models.ForeignKey(
        Mark,
        verbose_name='Марка',
        related_name='parts',
        on_delete=models.CASCADE,
    )
    model = models.ForeignKey(
        Model,
        verbose_name='Модель',
        related_name='parts',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2
    )
    json_data = models.JSONField()

    class Meta:
        verbose_name = 'запчасть'
        verbose_name_plural = 'Запчасти'
