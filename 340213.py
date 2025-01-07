#  동영상 재생기  https://school.programmers.co.kr/learn/courses/30/lessons/340211

def time_to_int(time):
    m,s = time.split(':')
    return int(m)*60 + int(s)  


def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_int(video_len)
    pos = time_to_int(pos)
    op_start = time_to_int(op_start)
    op_end = time_to_int(op_end)

    for c in commands:
        if pos >= op_start:
            if pos <= op_end:
                pos = op_end
        if c == "next":
            pos += 10
            if pos > video_len:
                pos = video_len
        elif c == "prev":
            pos -= 10 
            if pos < 0 :
                pos = 0
    if pos >= op_start:
        if pos <= op_end:
            pos = op_end


    return str(pos//60).zfill(2)+":"+str(pos%60).zfill(2)

