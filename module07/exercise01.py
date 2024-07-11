"""
1. Exception -> Failures
Type I Error -> Fix -> Maintenance -> Exception
Type II Error -> File/DB/Kafka/UI  -> Exception

2. File: I/O Operations
File -> Persistence
data -> memory: list/set/tuples/dict -> persist -> file
        file: i. text i/o
             ii. binary i/o

Serialization (structured data):
1. csv, json, xml -> text i/0 -> hrf
   cross platform
2. pickle -> binary -> python
3. protocol buffers -> binary -> cross platform
   cncf: https://www.cncf.io/
   parquet -> binary -> big data analytics, dwh
"""