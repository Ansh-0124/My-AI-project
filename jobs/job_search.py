"""
Job Search Module
=================
Provides a Streamlit-based job search interface that
searches for job listings using web APIs.
"""

import streamlit as st
import requests
import json
from urllib.parse import quote_plus


def render_job_search():
    """Render the job search page in Streamlit."""
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2rem; border-radius: 15px; margin-bottom: 2rem;
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);">
        <h1 style="color: white; text-align: center; margin: 0;">
            🎯 Job Search Engine
        </h1>
        <p style="color: rgba(255,255,255,0.8); text-align: center; margin-top: 0.5rem;">
            Find your next opportunity across top job platforms
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Search form
    col1, col2, col3 = st.columns([3, 2, 1])
    
    with col1:
        job_title = st.text_input(
            "🔍 Job Title / Keywords",
            placeholder="e.g., Software Engineer, Data Scientist...",
            key="job_search_title"
        )
    
    with col2:
        location = st.text_input(
            "📍 Location",
            placeholder="e.g., New York, Remote...",
            key="job_search_location"
        )
    
    with col3:
        experience = st.selectbox(
            "💼 Experience",
            ["All", "Entry Level", "Mid Level", "Senior", "Lead/Manager"],
            key="job_search_experience"
        )
    
    # Search button
    search_clicked = st.button("🔍 Search Jobs", use_container_width=True, type="primary")
    
    st.markdown("---")
    
    if search_clicked and job_title:
        _display_job_results(job_title, location, experience)
    elif search_clicked and not job_title:
        st.warning("⚠️ Please enter a job title or keywords to search.")
    else:
        _display_job_platforms()


def _display_job_results(job_title, location, experience):
    """Display job search results with links to major platforms."""
    
    encoded_title = quote_plus(job_title)
    encoded_location = quote_plus(location) if location else ""
    
    st.subheader(f"🔎 Results for: **{job_title}**" + (f" in {location}" if location else ""))
    
    # Generate search links for major platforms
    platforms = [
        {
            "name": "LinkedIn",
            "icon": "💼",
            "url": f"https://www.linkedin.com/jobs/search/?keywords={encoded_title}&location={encoded_location}",
            "color": "#0077B5",
            "description": "Professional network with millions of job listings"
        },
        {
            "name": "Indeed",
            "icon": "🔵",
            "url": f"https://www.indeed.com/jobs?q={encoded_title}&l={encoded_location}",
            "color": "#2164f3",
            "description": "World's #1 job site with millions of listings"
        },
        {
            "name": "Glassdoor",
            "icon": "🟢",
            "url": f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={encoded_title}&locT=C&locKeyword={encoded_location}",
            "color": "#0caa41",
            "description": "Jobs with company reviews and salary data"
        },
        {
            "name": "Naukri.com",
            "icon": "🔴",
            "url": f"https://www.naukri.com/{encoded_title.replace('+', '-')}-jobs",
            "color": "#4a90d9",
            "description": "India's #1 job portal"
        },
        {
            "name": "Google Jobs",
            "icon": "🔍",
            "url": f"https://www.google.com/search?q={encoded_title}+jobs+{encoded_location}&ibp=htl;jobs",
            "color": "#4285f4",
            "description": "Aggregated listings from across the web"
        },
        {
            "name": "AngelList / Wellfound",
            "icon": "👼",
            "url": f"https://wellfound.com/jobs?q={encoded_title}",
            "color": "#000000",
            "description": "Startup and tech company jobs"
        },
    ]
    
    # Display platform cards
    for i in range(0, len(platforms), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(platforms):
                platform = platforms[i + j]
                with col:
                    st.markdown(f"""
                    <div style="background: rgba(45, 45, 45, 0.9); border-radius: 15px;
                                padding: 1.5rem; margin-bottom: 1rem;
                                border-left: 4px solid {platform['color']};
                                transition: transform 0.2s;">
                        <h3 style="margin: 0 0 0.5rem 0;">{platform['icon']} {platform['name']}</h3>
                        <p style="color: #b0b0b0; margin: 0 0 1rem 0; font-size: 0.9rem;">
                            {platform['description']}
                        </p>
                        <a href="{platform['url']}" target="_blank" 
                           style="background: {platform['color']}; color: white; 
                                  padding: 0.5rem 1.5rem; border-radius: 8px;
                                  text-decoration: none; font-weight: 600;
                                  display: inline-block;">
                            Search on {platform['name']} →
                        </a>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Tips section
    st.markdown("---")
    st.subheader("💡 Job Search Tips")
    
    tips = [
        "**Tailor your resume** for each application — use keywords from the job description.",
        "**Set up job alerts** on LinkedIn and Indeed to be notified of new openings.",
        "**Network actively** — 70% of jobs are found through networking.",
        "**Research companies** on Glassdoor before applying to understand culture and compensation.",
        "**Follow up** on applications after 1-2 weeks with a polite email.",
        "**Practice common interview questions** using the STAR method.",
    ]
    
    for tip in tips:
        st.markdown(f"• {tip}")


def _display_job_platforms():
    """Display popular job platforms when no search is active."""
    
    st.subheader("🌐 Popular Job Platforms")
    st.markdown("Start your job search on these top platforms:")
    
    platforms = {
        "💼 LinkedIn": "https://www.linkedin.com/jobs/",
        "🔵 Indeed": "https://www.indeed.com/",
        "🟢 Glassdoor": "https://www.glassdoor.com/",
        "🔴 Naukri": "https://www.naukri.com/",
        "👼 Wellfound": "https://wellfound.com/jobs",
        "💻 HackerRank Jobs": "https://www.hackerrank.com/jobs/search",
    }
    
    cols = st.columns(3)
    for i, (name, url) in enumerate(platforms.items()):
        with cols[i % 3]:
            st.markdown(f"""
            <a href="{url}" target="_blank" style="text-decoration: none;">
                <div style="background: rgba(45, 45, 45, 0.9); border-radius: 12px;
                            padding: 1.5rem; text-align: center; margin-bottom: 1rem;
                            transition: transform 0.2s; cursor: pointer;
                            border: 1px solid rgba(255,255,255,0.1);">
                    <h3 style="color: white; margin: 0;">{name}</h3>
                </div>
            </a>
            """, unsafe_allow_html=True)
    
    # Quick stats
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🌍 Platforms", "6+")
    with col2:
        st.metric("📊 Job Listings", "Millions")
    with col3:
        st.metric("🎯 Categories", "20+")
    with col4:
        st.metric("🌐 Coverage", "Global")
