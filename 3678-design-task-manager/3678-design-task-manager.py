class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_user = defaultdict(int)
        self.task_priority = defaultdict(int)
        self.taskList = []

        for userID, taskID, priority in tasks:
            self.task_user[taskID] = userID
            self.task_priority[taskID] = priority
            heappush(self.taskList, (-priority, -taskID))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_user[taskId] = userId
        self.task_priority[taskId] = priority
        heappush(self.taskList, (-priority, -taskId)) 

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_priority[taskId] = newPriority
        heappush(self.taskList, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.task_priority[taskId]
        del self.task_user[taskId]

    def execTop(self) -> int:
        while self.taskList and (-self.taskList[0][1] not in self.task_priority or -self.taskList[0][0] != self.task_priority[-self.taskList[0][1]]):
            heappop(self.taskList)
        
        ans = -1
        if self.taskList:
            taskId = -heappop(self.taskList)[1]
            ans = self.task_user[taskId]
            del self.task_priority[taskId]
            del self.task_user[taskId]
        return ans


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()