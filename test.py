import datetime

# ----------------------------------------------
# 1) 예시 데이터 (실제 DB 대신 사용)
# ----------------------------------------------
users = [
    {"user_id": 1, "user_name": "홍길동", "email": "hong@test.com"},
    {"user_id": 2, "user_name": "김철수", "email": "kim@test.com"}
]

webtoons = [
    {"webtoon_id": 101, "title": "재밌는 웹툰1", "author": "작가1", "genre": "액션"},
    {"webtoon_id": 102, "title": "재밌는 웹툰2", "author": "작가2", "genre": "로맨스"}
]

episodes = [
    {"episode_id": 1001, "webtoon_id": 101, "ep_number": 1, "ep_title": "1화 시작"},
    {"episode_id": 1002, "webtoon_id": 101, "ep_number": 2, "ep_title": "2화 대결"},
    {"episode_id": 1003, "webtoon_id": 101, "ep_number": 3, "ep_title": "3화 결과"},
    
    {"episode_id": 2001, "webtoon_id": 102, "ep_number": 1, "ep_title": "첫만남"},
    {"episode_id": 2002, "webtoon_id": 102, "ep_number": 2, "ep_title": "오해"},
    {"episode_id": 2003, "webtoon_id": 102, "ep_number": 3, "ep_title": "진실"}
]

user_readings = [
    {"user_id": 1, "webtoon_id": 101, "episode_id": 1001, "is_read": True,  "read_date": "2025-01-01"},
    {"user_id": 1, "webtoon_id": 101, "episode_id": 1002, "is_read": True,  "read_date": "2025-01-02"},
    {"user_id": 1, "webtoon_id": 101, "episode_id": 1003, "is_read": False, "read_date": None},
    
    {"user_id": 1, "webtoon_id": 102, "episode_id": 2001, "is_read": True,  "read_date": "2025-01-03"},
    # 2002, 2003 에피소드는 아직 기록 없음 -> 안 봄
    
    {"user_id": 2, "webtoon_id": 101, "episode_id": 1001, "is_read": False, "read_date": None},
    # ...
]

# ----------------------------------------------
# 2) 함수(서비스 로직)
# ----------------------------------------------

def get_episodes_for_webtoon(webtoon_id):
    """
    특정 웹툰에 해당하는 모든 에피소드 목록을 반환
    """
    return [ep for ep in episodes if ep["webtoon_id"] == webtoon_id]

def get_user_reading_status(user_id, webtoon_id):
    """
    특정 사용자가 특정 웹툰의 에피소드를 본 기록 리스트를 반환
    """
    return [ur for ur in user_readings
            if ur["user_id"] == user_id and ur["webtoon_id"] == webtoon_id]

def check_unread_episodes(user_id, webtoon_id):
    """
    사용자가 아직 안 본 에피소드 목록을 찾아 리턴
    """
    all_ep = get_episodes_for_webtoon(webtoon_id)          # 전체 에피소드
    read_status_list = get_user_reading_status(user_id, webtoon_id)  # 본 기록
    
    # episode_id를 키로, is_read를 값으로 하는 dict 생성
    read_dict = {rs["episode_id"]: rs["is_read"] for rs in read_status_list}
    
    # 안 본 에피소드만 걸러내기
    unread_list = []
    for ep in all_ep:
        ep_id = ep["episode_id"]
        if ep_id not in read_dict or not read_dict[ep_id]:
            unread_list.append(ep)
    
    return unread_list

def print_unread_episodes(user_id, webtoon_id):
    """
    사용자가 아직 안 본 에피소드를 화면에 출력
    """
    unread_list = check_unread_episodes(user_id, webtoon_id)
    if not unread_list:
        print(f"[웹툰 ID: {webtoon_id}] 아직 안 본 에피소드가 없습니다.")
    else:
        print(f"[웹툰 ID: {webtoon_id}] 아직 안 본 에피소드 목록:")
        for ep in unread_list:
            print(f" - 에피소드 번호: {ep['ep_number']}, 제목: {ep['ep_title']}")

def mark_episode_as_read(user_id, webtoon_id, episode_id):
    """
    특정 사용자가 특정 웹툰의 특정 에피소드를 봤다고 표시
    이미 본 기록이 있으면 갱신, 없으면 새로 추가
    """
    found_record = None
    for ur in user_readings:
        if (ur["user_id"] == user_id 
            and ur["webtoon_id"] == webtoon_id 
            and ur["episode_id"] == episode_id):
            found_record = ur
            break
    
    if found_record:
        # 이미 기록이 있는 경우 업데이트
        found_record["is_read"] = True
        found_record["read_date"] = datetime.date.today().isoformat()
    else:
        # 기록이 없는 경우 새로 추가
        user_readings.append({
            "user_id": user_id,
            "webtoon_id": webtoon_id,
            "episode_id": episode_id,
            "is_read": True,
            "read_date": datetime.date.today().isoformat()
        })
    print(f"에피소드 {episode_id} 시청 처리가 완료되었습니다.")

# ----------------------------------------------
# 3) 메인 실행
# ----------------------------------------------

def main():
    user_id = 1  # 홍길동(예시)

    print("=== 1) 아직 안 본 에피소드 확인 ===")
    print_unread_episodes(user_id, 101)
    print()
    
    print("=== 2) 에피소드 1003 시청 처리 ===")
    mark_episode_as_read(user_id, 101, 1003)
    print()
    
    print("=== 3) 다시 확인 (웹툰 101) ===")
    print_unread_episodes(user_id, 101)
    print()
    
    print("=== 4) 웹툰 102 확인 ===")
    print_unread_episodes(user_id, 102)
    print()
    

if __name__ == "__main__":
    main()