from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_student_found = (name, score) = ("",0)
    for student, score in scores:
        if score > best_student_found[1]:
            best_student_found = (student, score)
    
    return best_student_found[0]


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
