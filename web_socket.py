from fastapi import APIRouter, WebSocket, WebSocketDisconnect


class WebSocketManager():
    _websockets: dict[str, set[WebSocket]]

    def __init__(self) -> None:
        self._websockets = dict()

    def add(self, oid: str, websocket: WebSocket):
        if self._websockets.get(oid) is None:
            self._websockets[oid] = {websocket,}
        else:
            self._websockets[oid].add(websocket)

    def remove(self, oid: str, websocket: WebSocket):
        self._websockets[oid].remove(websocket)
        if len(self._websockets[oid]) == 0:
            self._websockets.pop(oid)

    async def send(self, oid: str, sender: WebSocket, data):
        for receiver in self._websockets[oid]:
            if receiver != sender:
                await receiver.send_json(data)

    def __str__(self) -> str:
        return str(self._websockets)

ws_manager = WebSocketManager()
router = APIRouter()


@router.websocket("/ws/{diagram_oid}")
async def websocket_endpoint(websocket: WebSocket, diagram_oid: str):
    await websocket.accept()
    ws_manager.add(diagram_oid, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await ws_manager.send(diagram_oid, websocket, data)
    except WebSocketDisconnect:
        ws_manager.remove(diagram_oid, websocket)
