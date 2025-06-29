### Upload Single Document
- **POST** `/upload`
- Accepts a single PDF document in French
- Returns confirmation of processing and number of chunks created

### Upload Folder of Documents
- **POST** `/upload_folder`
- Accepts a `folder_path` as a string in the request body.
- Iterates through all PDF files in the specified folder and its subfolders.
- Returns a summary of indexed and failed files.

### Query Document
- **POST** `/query`
- Send questions in JSON format:
  ```json
  {
    "question": "Your question in French",
    "chat_history": [["previous question", "previous answer"]]
  }
  ```
- Returns answer and source documents