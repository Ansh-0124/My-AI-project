"""
Feedback Module
===============
Manages user feedback collection, storage, and display
for the Smart Resume AI application.
"""

import streamlit as st
import datetime
import json
import os


class FeedbackManager:
    """
    Manages user feedback for the application.
    Stores feedback in a local JSON file.
    """
    
    FEEDBACK_FILE = "feedback_data.json"
    
    def __init__(self):
        self.feedback_data = self._load_feedback()
    
    def _load_feedback(self):
        """Load existing feedback from file."""
        if os.path.exists(self.FEEDBACK_FILE):
            try:
                with open(self.FEEDBACK_FILE, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, Exception):
                return []
        return []
    
    def _save_feedback(self):
        """Save feedback to file."""
        try:
            with open(self.FEEDBACK_FILE, "w") as f:
                json.dump(self.feedback_data, f, indent=2, default=str)
        except Exception as e:
            st.error(f"Error saving feedback: {e}")
    
    def submit_feedback(self, name, email, rating, category, feedback_text):
        """
        Submit new feedback.
        
        Parameters
        ----------
        name : str
            User's name
        email : str
            User's email
        rating : int
            Rating from 1-5
        category : str
            Feedback category
        feedback_text : str
            Detailed feedback message
        """
        feedback_entry = {
            "id": len(self.feedback_data) + 1,
            "name": name,
            "email": email,
            "rating": rating,
            "category": category,
            "feedback": feedback_text,
            "timestamp": datetime.datetime.now().isoformat(),
        }
        
        self.feedback_data.append(feedback_entry)
        self._save_feedback()
        return feedback_entry
    
    def get_all_feedback(self):
        """Get all feedback entries."""
        return self.feedback_data
    
    def get_average_rating(self):
        """Calculate average rating."""
        if not self.feedback_data:
            return 0
        ratings = [f.get("rating", 0) for f in self.feedback_data]
        return sum(ratings) / len(ratings)
    
    def get_feedback_count(self):
        """Get total feedback count."""
        return len(self.feedback_data)
    
    def render_feedback_form(self):
        """Render the feedback form in Streamlit."""
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                    padding: 2rem; border-radius: 15px; margin-bottom: 2rem;
                    box-shadow: 0 10px 20px rgba(0,0,0,0.2);">
            <h1 style="color: white; text-align: center; margin: 0;">
                💬 We'd Love Your Feedback!
            </h1>
            <p style="color: rgba(255,255,255,0.8); text-align: center; margin-top: 0.5rem;">
                Help us improve Smart Resume AI
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📊 Total Feedback", self.get_feedback_count())
        with col2:
            avg = self.get_average_rating()
            st.metric("⭐ Average Rating", f"{avg:.1f}/5" if avg > 0 else "N/A")
        with col3:
            st.metric("😊 Satisfaction", 
                      f"{(avg/5*100):.0f}%" if avg > 0 else "N/A")
        
        st.markdown("---")
        
        # Feedback form
        with st.form("feedback_form", clear_on_submit=True):
            st.subheader("📝 Submit Your Feedback")
            
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("👤 Your Name", placeholder="John Doe")
            with col2:
                email = st.text_input("📧 Email (optional)", placeholder="john@example.com")
            
            rating = st.slider("⭐ Overall Rating", 1, 5, 4)
            
            category = st.selectbox("📂 Category", [
                "General Feedback",
                "Resume Analyzer",
                "Resume Builder",
                "AI Features",
                "UI/UX",
                "Bug Report",
                "Feature Request",
                "Other"
            ])
            
            feedback_text = st.text_area(
                "💬 Your Feedback",
                placeholder="Tell us what you think! What did you like? What can we improve?",
                height=150
            )
            
            submitted = st.form_submit_button("🚀 Submit Feedback", use_container_width=True)
            
            if submitted:
                if not name or not feedback_text:
                    st.error("❌ Please fill in your name and feedback message.")
                else:
                    self.submit_feedback(name, email, rating, category, feedback_text)
                    st.success("✅ Thank you for your feedback! We appreciate it.")
                    st.balloons()
        
        # Display recent feedback
        if self.feedback_data:
            st.markdown("---")
            st.subheader("📋 Recent Feedback")
            
            for entry in reversed(self.feedback_data[-5:]):
                stars = "⭐" * entry.get("rating", 0)
                st.markdown(f"""
                <div style="background: rgba(45, 45, 45, 0.9); border-radius: 12px;
                            padding: 1rem 1.5rem; margin-bottom: 0.8rem;
                            border-left: 3px solid #f5576c;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <strong>{entry.get('name', 'Anonymous')}</strong>
                        <span>{stars}</span>
                    </div>
                    <p style="color: #b0b0b0; margin: 0.5rem 0 0 0; font-size: 0.9rem;">
                        {entry.get('feedback', '')}
                    </p>
                    <small style="color: #666;">
                        {entry.get('category', '')} · {entry.get('timestamp', '')[:10]}
                    </small>
                </div>
                """, unsafe_allow_html=True)
