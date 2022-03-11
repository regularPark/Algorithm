# my code
def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        order = []
        for spell in skills:
            if spell in skill:
                order.append(spell)
            else:
                continue
        skill_order = "".join(order)
        if skill.startswith(skill_order):
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))


# 스킬트리에 있는 스킬들만 추출하고
# 그 순서를 startswith()로 스킬트리와 비교한다.
