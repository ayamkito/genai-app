# ...existing content...

## Setup Instructions

### Configure the `.env` File

1. Create a `.env` file in the root of the `backend` directory if it doesn't already exist.
2. Add the following line to the `.env` file, replacing `your_openai_api_key` with your actual OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

3. Save the file.

The application will automatically load the API key from the `.env` file when it starts.

### Install Backend Dependencies

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

This will install all the necessary Python packages listed in the `requirements.txt` file.

# ...existing content...
