from memory.memory_bank import MemoryBank
from agents.tutor_agent import TutorAgent
from agents.quiz_agent import QuizAgent
from agents.progress_agent import ProgressAgent
from tools.google_search_tool import MockSearchTool

def demo_session():
    mem = MemoryBank()
    mem.current_user = 'user_1'
    mem.register_tool('search', MockSearchTool())

    tutor = TutorAgent(memory=mem)
    quiz = QuizAgent(memory=mem)
    prog = ProgressAgent(memory=mem)

    topic = "Newton's Second Law"

    print("---- TUTOR EXPLANATION ----")
    print(tutor.explain(topic))

    print("\n---- QUIZ QUESTIONS ----")
    questions = quiz.generate_quiz(topic, n=4)
    for q in questions:
        print(q)

    user_answers = {
        questions[0]['id']: questions[0]['answer'],
        questions[1]['id']: questions[1]['answer'],
        questions[2]['id']: 'wrong',
        questions[3]['id']: 'wrong'
    }

    print("\n---- QUIZ EVALUATION ----")
    score, details = quiz.evaluate_answers(questions, user_answers)
    print(score)
    print(details)

    prog.record_results('user_1', topic, [d['correct'] for d in details])
    print("\n---- STUDY PLAN ----")
    print(prog.generate_study_plan('user_1'))

if __name__ == "__main__":
    demo_session()
