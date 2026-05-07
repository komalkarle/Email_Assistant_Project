"""
AI Smart Email Assistant using Streamlit
A beginner-friendly email reply generator using simple NLP logic
No paid APIs required!
"""

import streamlit as st
import re
from collections import Counter

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# HELPER FUNCTIONS - SIMPLE NLP FOR EMAIL DETECTION
# ============================================================================

def detect_email_type(email_text):
    """
    Detect email type using keyword matching (Simple NLP)
    Returns: (email_type, confidence_keywords)
    """
    email_lower = email_text.lower()
    
    # Define keyword patterns for each email type
    email_types = {
        "Meeting Request": [
            "meeting", "schedule", "calendar", "time slot", "availability",
            "call", "conference", "discussion", "sync", "check in"
        ],
        "Complaint": [
            "complaint", "issue", "problem", "broken", "not working", 
            "frustrated", "upset", "disappointed", "unhappy", "wrong",
            "error", "bug", "failed"
        ],
        "Job Related": [
            "job", "position", "interview", "hire", "recruitment", "resume",
            "application", "candidate", "salary", "offer", "interview",
            "cv", "employment", "vacancy"
        ],
        "General Email": []  # Default category
    }
    
    # Count matches for each category
    type_scores = {}
    for email_type, keywords in email_types.items():
        if email_type == "General Email":
            continue
        matches = sum(1 for keyword in keywords if keyword in email_lower)
        type_scores[email_type] = matches
    
    # Find the type with highest match
    if type_scores and max(type_scores.values()) > 0:
        # detected_type = max(type_scores, key=type_scores.get)
        detected_type = max(type_scores, key=lambda x: type_scores[x])
        matched_keywords = [
            kw for kw in email_types[detected_type] 
            if kw in email_lower
        ]
        return detected_type, matched_keywords
    
    return "General Email", []


def extract_key_info(email_text):
    """
    Extract basic information from email
    Returns: sender name, main topic
    """
    email_lower = email_text.lower()
    
    # Try to extract sender name (crude pattern matching)
    sender_patterns = [
        r"(?:from|from:).*?([A-Z][a-z]+)",
        r"(?:hello|hi|dear)\s+([A-Z][a-z]+)",
    ]
    
    sender_name = "there"
    for pattern in sender_patterns:
        match = re.search(pattern, email_text)
        if match:
            sender_name = match.group(1)
            break
    
    return sender_name


def generate_reply(original_email, email_type, tone, reply_style):
    """
    Generate a professional email reply using templates
    Based on email type, tone, and reply style
    """
    
    sender_name = extract_key_info(original_email)
    
    # Define reply templates based on email type and tone
    templates = {
        "Meeting Request": {
            "Formal": {
                "Short": f"Dear {sender_name},\n\nThank you for your meeting request. I would be pleased to discuss this further at your earliest convenience.\n\nBest regards",
                "Detailed": f"Dear {sender_name},\n\nThank you for reaching out to schedule a meeting. I appreciate the opportunity to connect and discuss this matter in detail. I am flexible with my calendar and can accommodate your preferred time slot. Please let me know your availability, and I will confirm the meeting promptly.\n\nI look forward to our discussion.\n\nBest regards",
                "Bullet Points": f"Dear {sender_name},\n\nThank you for your meeting request. Here's my response:\n\n• I am available for a meeting to discuss this matter\n• Please share your preferred time slots\n• I can adjust my schedule accordingly\n• Looking forward to our discussion\n\nBest regards"
            },
            "Friendly": {
                "Short": f"Hi {sender_name},\n\nThanks so much for reaching out! I'd love to chat about this. Let me know what works best for your schedule!\n\nCheers",
                "Detailed": f"Hi {sender_name},\n\nThanks for reaching out! I'm really excited to connect and discuss this with you. I have pretty good flexibility with my calendar, so just let me know what times work best for you, and I'll make it happen. Looking forward to chatting!\n\nCheers",
                "Bullet Points": f"Hi {sender_name},\n\nThanks for the meeting request! Here's what I'm thinking:\n\n• I'm definitely interested in meeting up\n• Flexible with timing – you pick what works\n• Happy to discuss via call, video, or in person\n• Let's make this happen!\n\nCheers"
            },
            "Apologetic": {
                "Short": f"Hi {sender_name},\n\nI sincerely apologize for any delay in response. I would be honored to meet with you. Please let me know your availability.\n\nSincerely",
                "Detailed": f"Hi {sender_name},\n\nI sincerely apologize for the delay in getting back to you. I appreciate you reaching out and would genuinely love to meet. I understand your time is valuable, so I'm committed to finding a time that works perfectly for you. Please share your availability, and I'll confirm immediately.\n\nThank you for your patience.\n\nSincerely",
                "Bullet Points": f"Hi {sender_name},\n\nI apologize for the delayed response. Regarding your meeting request:\n\n• I'm very interested in meeting with you\n• Sorry for the wait – please forgive me\n• I'm completely flexible with scheduling\n• Let's find a time that works for you\n\nSincerely"
            },
            "Strict": {
                "Short": f"Hello {sender_name},\n\nRegarding your meeting request: Please send calendar details and agenda items in advance.\n\nThanks",
                "Detailed": f"Hello {sender_name},\n\nI acknowledge your meeting request. To ensure productive use of both our time, please provide: (1) Specific agenda items, (2) Expected duration, (3) Proposed time slots with time zones. I will review and confirm accordingly.\n\nThanks",
                "Bullet Points": f"Hello {sender_name},\n\nRegarding your meeting request, I need the following:\n\n• Detailed agenda items\n• Expected meeting duration\n• Specific time options (with time zones)\n• Meeting format (call/video/in-person)\n• I will confirm once details are provided\n\nThanks"
            }
        },
        "Complaint": {
            "Formal": {
                "Short": f"Dear {sender_name},\n\nThank you for bringing this matter to our attention. We take your concerns seriously and will investigate immediately.\n\nSincerely",
                "Detailed": f"Dear {sender_name},\n\nThank you for bringing this issue to our attention. We sincerely apologize for the inconvenience this has caused you. Your feedback is invaluable to us, and we take all complaints seriously. We have initiated a thorough investigation and will work diligently to resolve this matter. We will follow up with you shortly with a detailed update.\n\nSincerely",
                "Bullet Points": f"Dear {sender_name},\n\nWe appreciate you reporting this issue. Here's our commitment:\n\n• We take your complaint seriously\n• Investigation initiated immediately\n• Detailed response within 24-48 hours\n• We'll make this right\n• Your satisfaction is our priority\n\nSincerely"
            },
            "Friendly": {
                "Short": f"Hi {sender_name},\n\nThanks for letting us know! We're really sorry about that. We're on it and will fix this for you!\n\nThanks",
                "Detailed": f"Hi {sender_name},\n\nFirst off, we're really sorry about what happened! We genuinely appreciate you taking the time to tell us about this issue. It's not the experience we want for our customers. We're looking into this right now and will make sure it's resolved. We'll be in touch very soon with a solution!\n\nThanks for being patient with us!",
                "Bullet Points": f"Hi {sender_name},\n\nWe're sorry this happened! Here's what we're doing:\n\n• Investigating the issue right now\n• We value your feedback\n• We'll make this right\n• Checking in with you very soon\n• Thanks for giving us a chance to fix it\n\nThanks!"
            },
            "Apologetic": {
                "Short": f"Dear {sender_name},\n\nI sincerely apologize for this issue. Please accept our heartfelt apologies. We will resolve this immediately.\n\nSincerely",
                "Detailed": f"Dear {sender_name},\n\nI cannot express enough how sorry we are for this situation. You deserved better, and we failed to meet your expectations. I personally apologize for the inconvenience and frustration this has caused you. We are taking immediate action to resolve this and ensure it doesn't happen again. Please give us the opportunity to make this right.\n\nSincerely",
                "Bullet Points": f"Dear {sender_name},\n\nWe are deeply sorry about this. Please know:\n\n• We apologize sincerely for this issue\n• This doesn't reflect our standards\n• We're fixing this immediately\n• We value you as a customer\n• We'll do better going forward\n\nSincerely"
            },
            "Strict": {
                "Short": f"Dear {sender_name},\n\nWe acknowledge your complaint. Please provide detailed documentation. Case assigned for resolution.\n\nThanks",
                "Detailed": f"Dear {sender_name},\n\nWe acknowledge receipt of your complaint. To expedite resolution, please provide: (1) Detailed description of the issue, (2) Screenshots/documentation, (3) Timeline of when it occurred, (4) Steps you've already taken. A case has been assigned. Response expected within 2 business days.\n\nThanks",
                "Bullet Points": f"Dear {sender_name},\n\nComplaint acknowledged. For resolution:\n\n• Provide detailed issue description\n• Include any relevant documentation\n• Specify date/time of occurrence\n• List steps already attempted\n• Case ID: [Will be assigned]\n• Resolution timeline: 2 business days\n\nThanks"
            }
        },
        "Job Related": {
            "Formal": {
                "Short": f"Dear {sender_name},\n\nThank you for this opportunity. I am very interested and would welcome the chance to discuss further.\n\nBest regards",
                "Detailed": f"Dear {sender_name},\n\nThank you for considering me for this opportunity. I am genuinely interested in this position and believe my skills and experience align well with your requirements. I would be delighted to discuss how I can contribute to your organization. Please let me know the next steps in the interview process.\n\nBest regards",
                "Bullet Points": f"Dear {sender_name},\n\nThank you for this opportunity. Here's my interest level:\n\n• Very interested in this position\n• My experience aligns with requirements\n• Ready to discuss my qualifications\n• Available for interview at your convenience\n• Looking forward to the opportunity\n\nBest regards"
            },
            "Friendly": {
                "Short": f"Hi {sender_name},\n\nThanks so much for reaching out! I'm really excited about this opportunity. Let's chat soon!\n\nCheers",
                "Detailed": f"Hi {sender_name},\n\nThanks for thinking of me for this role! I'm genuinely excited about the opportunity and the potential to grow with your team. Your company's work really resonates with me, and I think it could be a great fit. I'd love to learn more and discuss how I can contribute. Let me know when's a good time to chat!\n\nCheers",
                "Bullet Points": f"Hi {sender_name},\n\nThanks for the awesome opportunity! Here's my take:\n\n• Really excited about this position\n• Love what your company is doing\n• Think it could be a great fit\n• Ready to chat and learn more\n• Looking forward to connecting!\n\nCheers"
            },
            "Apologetic": {
                "Short": f"Dear {sender_name},\n\nThank you for this kind offer. I'm genuinely interested and apologize for any delayed response.\n\nBest regards",
                "Detailed": f"Dear {sender_name},\n\nThank you so much for this incredible opportunity. I apologize for any delay in my response – I wanted to give your offer the thoughtful consideration it deserves. I'm genuinely interested in this position and would love to move forward with the interview process. I appreciate your patience and understanding.\n\nBest regards",
                "Bullet Points": f"Dear {sender_name},\n\nThank you for this opportunity:\n\n• Very grateful and interested\n• Apologize for delayed response\n• Wanted to consider carefully\n• Ready to move forward\n• Looking forward to next steps\n• Thank you for your patience\n\nBest regards"
            },
            "Strict": {
                "Short": f"Hello {sender_name},\n\nI am interested. Please send job description, compensation details, and interview timeline.\n\nThanks",
                "Detailed": f"Hello {sender_name},\n\nI am interested in this position. Before proceeding, please provide: (1) Detailed job description, (2) Compensation range and benefits, (3) Interview timeline and process, (4) Required qualifications/experience. This will help me assess fit properly.\n\nThanks",
                "Bullet Points": f"Hello {sender_name},\n\nI'm interested. Need the following details:\n\n• Complete job description\n• Compensation and benefits package\n• Interview process and timeline\n• Required qualifications\n• Start date expectations\n• Please provide before next steps\n\nThanks"
            }
        },
        "General Email": {
            "Formal": {
                "Short": f"Dear {sender_name},\n\nThank you for your email. I appreciate you reaching out and look forward to discussing this further.\n\nBest regards",
                "Detailed": f"Dear {sender_name},\n\nThank you for your email. I have reviewed the contents and appreciate you bringing this to my attention. I find this matter important and would like to explore it further with you. I am available to discuss at your earliest convenience.\n\nBest regards",
                "Bullet Points": f"Dear {sender_name},\n\nThank you for reaching out:\n\n• I appreciate your email\n• Will review all details\n• Available to discuss further\n• Open to your suggestions\n• Looking forward to continuing\n\nBest regards"
            },
            "Friendly": {
                "Short": f"Hi {sender_name},\n\nThanks for getting in touch! I appreciate it and would love to chat about this.\n\nCheers",
                "Detailed": f"Hi {sender_name},\n\nThanks so much for reaching out! I really appreciate you thinking of me. Your email was great, and I'd love to continue this conversation. Let me know what works for you, and we can figure things out!\n\nCheers",
                "Bullet Points": f"Hi {sender_name},\n\nThanks for the email:\n\n• Really appreciate you reaching out\n• Great to hear from you\n• Happy to discuss further\n• Just let me know what you need\n• Looking forward to chatting!\n\nCheers"
            },
            "Apologetic": {
                "Short": f"Hi {sender_name},\n\nThank you for your email. I apologize for any inconvenience and appreciate your patience.\n\nSincerely",
                "Detailed": f"Hi {sender_name},\n\nThank you for your email. I sincerely apologize if I've caused any inconvenience or if there's been any misunderstanding. Your message is important to me, and I want to make sure we address everything properly. I appreciate your patience and understanding.\n\nSincerely",
                "Bullet Points": f"Hi {sender_name},\n\nThank you for your email:\n\n• I appreciate you reaching out\n• Apologize for any issues\n• Your concerns matter to me\n• Will address everything properly\n• Thank you for your patience\n\nSincerely"
            },
            "Strict": {
                "Short": f"Hello {sender_name},\n\nI received your email. Please provide specific details and expected outcomes for further discussion.\n\nThanks",
                "Detailed": f"Hello {sender_name},\n\nI have received your email. To address this effectively, please provide: (1) Specific details of your request, (2) Expected outcomes, (3) Timeline for decision, (4) Any supporting documentation. I will respond accordingly once I have all necessary information.\n\nThanks",
                "Bullet Points": f"Hello {sender_name},\n\nI received your email. Please provide:\n\n• Specific details of your request\n• Expected outcomes or goals\n• Timeline required\n• Supporting documentation\n• Any other relevant information\n• Will respond once details received\n\nThanks"
            }
        }
    }
    
    # Get the reply from template
    reply = templates.get(email_type, {}).get(tone, {}).get(reply_style, "")
    
    if not reply:
        # Fallback reply if template not found
        reply = f"Hello {sender_name},\n\nThank you for your email. I appreciate you reaching out.\n\nBest regards"
    
    return reply


# ============================================================================
# STREAMLIT UI
# ============================================================================

# Title and description
st.title("📧 AI Smart Email Assistant")
st.markdown("""
    *A simple, no-API email reply generator using intelligent keyword detection and professional templates.*
""")

# Create two columns for better layout
col1, col2 = st.columns([1, 1], gap="large")

# ============================================================================
# LEFT COLUMN - INPUT
# ============================================================================
with col1:
    st.subheader("📩 Email Input")
    
    # Email textarea
    email_input = st.text_area(
        "Paste the email you received:",
        height=250,
        placeholder="Paste your received email here and let AI detect the type and generate a professional reply...",
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    st.subheader("⚙️ Reply Settings")
    
    # Tone selector
    tone_option = st.selectbox(
        "Select Tone:",
        ["Formal", "Friendly", "Apologetic", "Strict"],
        help="Choose the tone for your reply"
    )
    
    # Reply style selector
    style_option = st.selectbox(
        "Reply Type:",
        ["Short", "Detailed", "Bullet Points"],
        help="Choose how detailed you want the reply"
    )
    
    # Generate button
    generate_btn = st.button(
        "🚀 Generate Reply",
        use_container_width=True,
        type="primary"
    )

# ============================================================================
# RIGHT COLUMN - OUTPUT
# ============================================================================
with col2:
    st.subheader("📋 AI-Generated Reply")
    
    if generate_btn:
        if email_input.strip() == "":
            st.warning("⚠️ Please paste an email first!", icon="⚠️")
        else:
            # Detect email type
            detected_type, matched_keywords = detect_email_type(email_input)
            
            # Show detection info
            st.info(f"**📌 Email Type Detected:** {detected_type}")
            if matched_keywords:
                st.caption(f"Keywords found: {', '.join(matched_keywords)}")
            
            st.markdown("---")
            
            # Generate reply
            reply_text = generate_reply(
                email_input,
                detected_type,
                tone_option,
                style_option
            )
            
            # Display reply in a nice format
            st.markdown("**Generated Reply:**")
            st.text_area(
                "Your email reply:",
                value=reply_text,
                height=300,
                disabled=True,
                label_visibility="collapsed"
            )
            
            # Copy button
            st.success("✅ Reply generated successfully!", icon="✅")
    else:
        st.info("👈 Enter an email and click 'Generate Reply' to get started!", icon="ℹ️")

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: gray; font-size: 12px;">
        Made with ❤️ using Streamlit | No paid APIs required | Beginner-friendly Python
    </div>
""", unsafe_allow_html=True)