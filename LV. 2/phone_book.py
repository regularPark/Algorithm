# my code, BEST code와 거의 유사
def solution(phone_book):
    phone_book.sort()
    len_b = len(phone_book)
    for i in range(1, len_b):
        if phone_book[i].startswith(phone_book[i-1]) == True:
            return False
        else:
            continue
    return True


# using Hash
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False

    return answer


print(solution(["119", "97674223", "1195524421"]))
