import re
import time
from datetime import datetime

class SleepingGuards:
    def __init__(self, lines):
        self.messages = self.parse_messages(lines)
        self.guards_schedule = {} #id: tuple of times asleep

    def find_most_minutes_asleep(self):
        guards = {} #id: minutes asleep
        current_guard = -1
        sleep_start = 0
        for (timestamp, message) in self.messages:
            if type(message) is int:
                current_guard = message #TODO implement
            elif 'falls' in message:
                sleep_start = timestamp #TODO implement
            elif 'wakes' in message:
                total = timestamp - sleep_start
                if current_guard in guards:
                    total += guards[current_guard]
                guards.update({current_guard : total})
                if current_guard not in self.guards_schedule:
                    self.guards_schedule[current_guard] = []
                self.guards_schedule[current_guard].append((sleep_start, timestamp))
            else:
                print('ERROR: mismatched messages')
        guard_id = max(guards, key=lambda key: guards[key])
        return guard_id

    def find_time_most_asleep(self, guard):
        timetable = [0 for _ in range(0, 59)]
        for (start, end) in self.guards_schedule[guard]:
            for i in range(start.time().minute, end.time().minute):
                timetable[i] += 1
        return timetable.index(max(timetable))

    #regular expressions
    # all things: ^\[[0-9]{4}(-[0-9]{2}){2} [0-9]{2}:[0-9]{2}\] (Guard #[0-9]* begins shift|falls asleep|wakes up)$
    # all things w/ \d: ^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}] (Guard #\d* begins shift|falls asleep|wakes up)$
    # delimteters: ^\[|-| |:\]|Guard #| begins shift$

    def parse_messages(self, lines):
        date_fmt = '\[|\] '
        lines.sort()
        res = []
        for message in lines:
            message = message.strip()
            message = re.split(date_fmt, message)
            message = list(filter(None, message))
            message[0] = self.convert_time(message[0])
            message[1] = self.condense_message(message[1])
            res.append(message)
        return res

    def convert_time(self, message):
        return datetime.strptime(message, '%Y-%m-%d %H:%M')

    def condense_message(self, message):
        message = re.split('Guard #| begins shift', message)
        if len(message) > 1:
            return (int)(message[1])
        return message[0]


file = open('day_4_input.txt', 'r')
messages = file.readlines()
file.close()
sched = SleepingGuards(messages)
guard_id = sched.find_most_minutes_asleep()
print('Guard #{id} spend the most time asleep'.format(id=guard_id))
time = sched.find_time_most_asleep(guard_id)
print('Guard #{id} slept most often at minute {min} '.format(id=guard_id, min=time))
print('answer is {ans}'.format(ans=guard_id*time))
