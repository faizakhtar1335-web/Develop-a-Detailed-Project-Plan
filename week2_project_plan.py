"""
Week 2 Task: Develop a Detailed Project Plan
Project: E-Commerce Platform

This script stores the project plan in structured Python data and prints:
- project overview
- detailed task breakdown
- resource allocation
- milestone timeline
- risk management plan
- overall effort estimate
"""

PROJECT = {
    "name": "Scalable E-Commerce Platform",
    "duration_weeks": 12,
    "goal": "Design and implement a secure, scalable e-commerce platform "
            "supporting user registration, product browsing, shopping cart, "
            "checkout, payment processing, and order management.",
}

TASKS = [
    ("T01", "Project initiation & requirements", "Planning", 1, 5),
    ("T02", "Architecture & database design", "Design", 2, 5),
    ("T03", "UI/UX design", "Design", 2, 5),
    ("T04", "User authentication service", "Development", 3, 7),
    ("T05", "Product catalog service", "Development", 3, 7),
    ("T06", "Cart & order service", "Development", 5, 7),
    ("T07", "Payment integration", "Development", 6, 7),
    ("T08", "Frontend implementation", "Development", 4, 9),
    ("T09", "API integration & system integration", "Integration", 8, 10),
    ("T10", "Testing & security validation", "Testing", 9, 11),
    ("T11", "Deployment & production setup", "Deployment", 11, 12),
    ("T12", "Documentation & handover", "Closure", 11, 12),
]

RESOURCES = [
    ("Project Manager", 1, "Planning, coordination, tracking, risk management"),
    ("Backend Developer", 2, "APIs, services, database integration"),
    ("Frontend Developer", 1, "Web interface and frontend integration"),
    ("UI/UX Designer", 1, "Wireframes, prototypes, usability"),
    ("QA Engineer", 1, "Functional, integration, regression testing"),
    ("DevOps Engineer", 1, "CI/CD, cloud, deployment, monitoring"),
    ("Security Specialist", 0.5, "Security review and vulnerability testing"),
]

MILESTONES = [
    ("M1", "Requirements approved", "Week 1", "Scope and requirements baseline completed"),
    ("M2", "Architecture approved", "Week 2", "Architecture and database design finalized"),
    ("M3", "Core services ready", "Week 7", "Authentication, catalog, cart/order and payment components available"),
    ("M4", "Feature-complete build", "Week 9", "Frontend and backend integrated"),
    ("M5", "Testing sign-off", "Week 11", "Critical defects resolved and release candidate approved"),
    ("M6", "Production release", "Week 12", "Platform deployed and handed over"),
]

RISKS = [
    ("R1", "Requirements changes", "Medium", "High",
     "Use requirements baseline, change requests and impact analysis."),
    ("R2", "Third-party payment/API failure", "Medium", "High",
     "Use sandbox testing, retries, timeouts and a fallback error flow."),
    ("R3", "Security vulnerability", "Medium", "Very High",
     "Apply secure coding, authentication controls, dependency scanning and security testing."),
    ("R4", "Schedule delay", "Medium", "High",
     "Track weekly progress, prioritize critical-path tasks and maintain contingency."),
    ("R5", "Performance/scalability issues", "Medium", "High",
     "Load-test key APIs and use caching, indexing and scalable infrastructure."),
    ("R6", "Data loss or corruption", "Low", "Very High",
     "Automated backups, database constraints, recovery procedures and monitoring."),
]

def total_estimated_team_weeks():
    # Approximate staffing over the 12-week project.
    return 12 * sum(resource[1] for resource in RESOURCES)

def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def print_plan():
    print_section("PROJECT OVERVIEW")
    print(f"Project: {PROJECT['name']}")
    print(f"Duration: {PROJECT['duration_weeks']} weeks")
    print(f"Goal: {PROJECT['goal']}")

    print_section("DETAILED TASK BREAKDOWN")
    print(f"{'ID':<5} {'Task':<42} {'Phase':<15} {'Start':<7} {'End':<7}")
    for task in TASKS:
        task_id, name, phase, start, end = task
        print(f"{task_id:<5} {name:<42} {phase:<15} W{start:<6} W{end:<6}")

    print_section("RESOURCE ALLOCATION")
    for role, count, responsibility in RESOURCES:
        print(f"- {role}: {count} FTE | {responsibility}")

    print_section("MILESTONES")
    for milestone_id, name, week, criteria in MILESTONES:
        print(f"{milestone_id}: {name} ({week}) - {criteria}")

    print_section("RISK MANAGEMENT")
    for risk_id, risk, probability, impact, mitigation in RISKS:
        print(f"{risk_id}: {risk} | Probability: {probability} | Impact: {impact}")
        print(f"    Mitigation: {mitigation}")

    print_section("ESTIMATE")
    print(f"Approximate team capacity: {total_estimated_team_weeks():.1f} person-weeks")
    print("Note: This is a planning estimate, not a project accounting figure.")

if __name__ == "__main__":
    print_plan()
