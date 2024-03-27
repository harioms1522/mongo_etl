# mongo_etl

### Pipeline
    - At one time only one pipeline can be processed
    - On a single collection
    - 

### connection can be accessed for mongodb usi8ng the connector
    - multiple connections can be created using that

### Extractors
    - Will maintain the metadata of the data that was extracted 
    - data will be loaded in batches and processed in batches
    - its responsibility is to
        - Get the mongodb documents 
        - Apply the schema mappers

### Data Streams
    - Updated batch data will flow to next stages in pipeline

### Schema Mapper
    - a script or an object that represents the exact recent fully updated document can be added to create the schema
    - by sampling of the data we can determine the schema
    - Schema can be mapped and fields can be determined
    - shcema determined will be stored as a metadata for now and will be used at the time of loading to load in that structure

### Flow
    - IN cli we will present all the collections than can be extracted
    - user will choose
    - we will load the data from that collection
        - He can want 
            - The incremental data 
            - Or the whole data
            - some filter can be applied to get the data from the extractor
        - We will show the output
            - table schemas that will be created
            - number of documents that will be added 


