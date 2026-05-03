def generate_paper(client, subject, context, difficulty, plan, year, time, duration):

    structure = "\n".join([f"{k}: {v} questions" for k, v in plan.items()])

    prompt = f"""
Generate a question paper in ANNA UNIVERSITY format.

Rules:
- Plain text only
- No markdown symbols

Format:

ANNA UNIVERSITY
B.E / B.Tech DEGREE EXAMINATION

Subject: {subject}
Year: {year}
Time: {time}
Duration: {duration}

--------------------------------------

{structure}

Syllabus:
{context}

Instructions:
- Proper spacing
- Number questions
- Mention marks clearly
"""

    chat = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )

    return chat.choices[0].message.content