<<<<<<< HEAD
# 📧 AI Smart Email Assistant

A beginner-friendly Streamlit application that automatically detects email types and generates professional replies without requiring any paid APIs.

## Features ✨

1. **Email Type Detection** - Automatically identifies if an email is about:
   - Meeting Request
   - Complaint
   - Job Opportunity
   - General Inquiry

2. **Tone Selection** - Choose your reply tone:
   - Formal
   - Friendly
   - Apologetic
   - Strict

3. **Reply Format** - Select how detailed:
   - Short (1-2 sentences)
   - Detailed (Full paragraph)
   - Bullet Points (Structured format)

4. **Smart Generation** - Creates professional, context-aware replies based on email content, tone, and format

## How It Works 🔍

The app uses simple, **beginner-friendly NLP logic**:
- **Keyword Matching**: Scans email for keywords to detect type
- **Template System**: Uses professional reply templates
- **Sender Detection**: Extracts sender name for personalization
- **No APIs**: Everything runs locally with zero dependencies on external services

## Installation 🚀

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**:
   ```bash
   streamlit run app.py
   ```

3. **Open in browser**: 
   - Streamlit will automatically open `http://localhost:8501`

## Usage 📝

1. **Paste an email** in the text area
2. **Select the tone** you want to use
3. **Choose reply type** (short, detailed, or bullet points)
4. **Click "Generate Reply"** to create your response
5. **Copy the generated reply** and use it!

## Code Structure 📚

### Main Functions:

- `detect_email_type()` - Uses keyword matching to categorize emails
- `extract_key_info()` - Extracts sender name for personalization
- `generate_reply()` - Retrieves appropriate template and generates reply

### Template System:

The app uses a nested dictionary with templates:
```
templates[email_type][tone][reply_style] = reply_text
```

This makes it **easy to customize** - just edit the templates!

## Customization 🎨

### Adding More Email Types:

1. Edit `detect_email_type()` function
2. Add keywords for your new type
3. Add template entries in `generate_reply()`

### Changing Reply Tone:

Simply edit the templates in the `generate_reply()` function. Each template is easy to understand and modify!

### Modifying Templates:

All reply templates are in the `templates` dictionary - no need to touch complex AI code. Just edit the text!

## Beginner-Friendly Design 💡

- **No Machine Learning**: Uses simple keyword matching
- **No Paid APIs**: Everything is free
- **Easy to Understand**: Well-commented code with clear function names
- **Easy to Modify**: Templates are plain text, easy to customize
- **No Complex Dependencies**: Only requires Streamlit

## File Structure 📁

```
Email_Assistant_Project/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Tips for Best Results 💪

1. **Paste complete emails** for better type detection
2. **Use Formal tone** for professional/corporate emails
3. **Use Friendly tone** for colleague communications
4. **Use Apologetic tone** for complaint responses
5. **Use Strict tone** for formal business needs

## Future Enhancement Ideas 🚀

- Add email templates library
- Support multiple languages
- Store reply history
- Add custom tone creation
- Email validation
- Attachment support

## License

Free to use and modify for personal/educational purposes.

---

**Made with ❤️ using Streamlit | No APIs Required | Beginner-Friendly Python**
=======
# Email_Assistant_Project
Email auto reply
>>>>>>> b6986166d4cda7cdd3d84e1b70b036e35dbbc7af
