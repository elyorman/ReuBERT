from src.api.interaction.interaction_resource_impl import InteractionResourceImpl
from src.api.response.response_factory import ResponseFactory
from src.application.input_text.input_text_processor_impl import InputTextProcessorImpl
from src.application.interaction.interaction_service import InteractionService
from src.domain.pipeline import Pipeline
from src.infrastructure.persistence.interaction.in_memory_input_text_repository import InMemoryInputTextRepository
from src.infrastructure.pipeline_steps.bert_model_wrapper import BertModelWrapper
from src.infrastructure.pipeline_steps.bert_natural_answer_postprocessor import BertNaturalAnswerPostprocessor


class CLIReuBERTApplicativeContext:

    def __init__(self):
        pass

    def initialize(self):
        self._initialize_domain_services()
        self._initialize_application_services()
        self._initialize_resources()

    def _initialize_domain_services(self):
        self.input_text_repository = InMemoryInputTextRepository()
        self.pipeline = Pipeline(BertModelWrapper(), BertNaturalAnswerPostprocessor())
        self.input_text_processor = InputTextProcessorImpl(self.input_text_repository, self.pipeline)

    def _initialize_application_services(self):
        self.interaction_service = InteractionService(self.input_text_processor)

    def _initialize_resources(self):
        response_factory = ResponseFactory()
        self.robot_interaction_resource = InteractionResourceImpl(self.interaction_service, response_factory)

    def execute(self):
        return self.robot_interaction_resource.execute()
