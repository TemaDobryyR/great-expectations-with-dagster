from dagster import MetadataValue, Output, asset
from dagster_ge.factory import GEContextResource
from great_expectations.render.renderer import ValidationResultsPageRenderer
from great_expectations.render.view import DefaultMarkdownPageView


@asset
def validate_data(data_context: GEContextResource):

    # предоставим контекст данных GE
    context = data_context.get_data_context()

    # запустим проверку на соответствие набору ожиданий
    results = context.run_checkpoint('my_checkpoint')

    # визуазлиция результатов проверки в Dagster требует вывода метаданных  
    validation_results_page_renderer = ValidationResultsPageRenderer(run_info_at_end=True)

    rendered_document_content_list = (
        validation_results_page_renderer.render_validation_operator_result(results)
    )
    md_str = " ".join(DefaultMarkdownPageView().render(rendered_document_content_list))

    return Output(
        value=results['success'],
        metadata={
            "Expectation Results": MetadataValue.md(md_str)
    })