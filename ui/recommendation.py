"""
=========================================================
HR Recommendation Engine
=========================================================
"""

import streamlit as st

def show_recommendation(leave_probability):

    st.markdown("---")

    st.header("💡 HR Recommendations")

    if leave_probability >= 80:

        st.error(
            """
### 🔴 High Attrition Risk

Recommended Actions

• Immediate HR meeting

• Salary review

• Manager discussion

• Career growth planning

• Improve work-life balance

• Conduct retention interview
"""
        )

    elif leave_probability >= 60:

        st.warning(
            """
### 🟠 Moderate Risk

Recommended Actions

• Monthly HR follow-up

• Employee engagement activities

• Training opportunities

• Performance feedback sessions
"""
        )

    elif leave_probability >= 40:

        st.info(
            """
### 🟡 Medium Risk

Recommended Actions

• Monitor employee satisfaction

• Encourage skill development

• Improve communication
"""
        )

    else:

        st.success(
            """
### 🟢 Low Risk

Employee appears engaged.

Continue:

• Career development

• Recognition programs

• Regular feedback

• Learning opportunities
"""
        )