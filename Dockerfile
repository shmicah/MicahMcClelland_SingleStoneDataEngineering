FROM python:latest
COPY DataFiles /DataFiles
COPY OutputFiles /OutputFiles
COPY TestFiles /TestFiles
COPY Modules /Modules
ADD main.py .
ADD Modules/ReadCSVFile.py .
ADD Modules/ReadParquetFile.py .
ADD Modules/WriteJSONFile.py .
RUN pip install pandas pyarrow
WORKDIR .
CMD [ "python", "./main.py" ]