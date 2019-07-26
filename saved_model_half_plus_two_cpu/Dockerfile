FROM tensorflow/serving
WORKDIR /models/half_plus_two
COPY . .
ENTRYPOINT ["tensorflow_model_server", "--rest_api_port=8501", "--model_name=half_plus_two", "--model_base_path=/models/half_plus_two"]