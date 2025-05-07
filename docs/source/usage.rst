Usage
=====

Here's a quick example of how to use **anyvec**:

.. code-block:: python

   from anyvec.client import AnyVecClient
   from anyvec.models import VectorizationPayload

   client = AnyVecClient("http://localhost:8000")

   # Process a PDF
   with open("example.pdf", "rb") as f:
       file_content = f.read()
   payload = VectorizationPayload(file_content=file_content, file_name="example.pdf")
   result = client.vectorize(payload)
   print("Vectorization result:", result)