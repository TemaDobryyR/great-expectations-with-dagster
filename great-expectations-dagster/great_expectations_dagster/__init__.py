from dagster import (Definitions, define_asset_job, file_relative_path,
                     load_assets_from_modules)
from dagster_ge.factory import GEContextResource
from great_expectations_dagster.assets import validate_data



defs = Definitions(
    assets=[
        validate_data
    ],
    jobs=[
        # задание, которое запустит материализацию нашего ассета
        define_asset_job(
            name='validate_data_job',
            selection=[validate_data]
        )
    ],
    resources={
        # для настройки контекста GE необходимо указать корень каталога GE
        # (путь к файлу great_exepctations.yaml)
        'data_context': GEContextResource(
            ge_root_dir=file_relative_path(__file__, '../../great_expectations')
        )
    }
)
