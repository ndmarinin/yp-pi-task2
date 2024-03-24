from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Server:
    host_id: int
    free_ram: int

    def __init__(self, host_id: int, free_ram: int = 128):
        self.host_id = host_id
        self.free_ram = free_ram

    def get_task(self, task_size: int):
        self.free_ram -= task_size

    def __repr__(self):
        return f"\nID={self.host_id}\tRAM={self.free_ram}\n"


SERVER_COUNT = 1000
servers = list([Server(x) for x in range(SERVER_COUNT)])


class VM(BaseModel):
    id: int
    size: int
    task: str


def find_server(task_size: int):
    global servers
    servers.sort(key=lambda x: x.free_ram)

    for server in servers:
        if server.free_ram >= task_size:
            server.get_task(task_size)
            return server
    return None


@app.post("/create_vm")
async def create_vm(vm: VM):
    server = find_server(vm.size)
    if server is None:
        return {"result": "NOT_OK"}

    return {"result": "OK", "host_id": server.host_id}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9024)
