# PHP Compatibility Routes for MuppetsServer
# Add these endpoints to handle PHP-style requests from the game app

from fastapi import APIRouter, Query, Request
from fastapi.responses import JSONResponse
import json

router = APIRouter(tags=["PHP Compatibility"])

# Basic PHP endpoints that the game app expects

@router.get("/auth.php")
@router.post("/auth.php")
async def auth_php(request: Request, user_id: int = None, token: str = None):
    """
    Authentication endpoint
    Mimics the original auth.php behavior
    """
    try:
        # If POST request, get body data
        if request.method == "POST":
            body = await request.json()
            user_id = body.get("user_id", user_id)
            token = body.get("token", token)
    except:
        pass
    
    # Return auth response
    return JSONResponse({
        "status": "success",
        "user_id": user_id,
        "authenticated": True,
        "session": token or "default_session"
    })


@router.get("/util.php")
@router.post("/util.php")
async def util_php(request: Request, action: str = None, user_id: int = None):
    """
    Utility endpoint
    Handles various game utility functions
    """
    try:
        if request.method == "POST":
            body = await request.json()
            action = body.get("action", action)
            user_id = body.get("user_id", user_id)
    except:
        pass
    
    # Handle different actions
    if action == "get_player":
        return JSONResponse({
            "user_id": user_id,
            "name": "Player",
            "level": 1,
            "exp": 0
        })
    elif action == "get_monsters":
        return JSONResponse({
            "monsters": [],
            "count": 0
        })
    elif action == "get_islands":
        return JSONResponse({
            "islands": [],
            "count": 0
        })
    else:
        return JSONResponse({
            "status": "success",
            "action": action
        })


@router.get("/game.php")
@router.post("/game.php")
async def game_php(request: Request):
    """
    Main game endpoint
    """
    try:
        if request.method == "POST":
            body = await request.json()
        else:
            body = {}
    except:
        body = {}
    
    return JSONResponse({
        "status": "success",
        "game_data": body
    })


@router.get("/data.php")
@router.post("/data.php")
async def data_php(request: Request, type: str = None):
    """
    Game data endpoint
    """
    try:
        if request.method == "POST":
            body = await request.json()
            type = body.get("type", type)
    except:
        pass
    
    # Return different data based on type
    if type == "monsters":
        return JSONResponse({
            "monsters": []
        })
    elif type == "islands":
        return JSONResponse({
            "islands": []
        })
    else:
        return JSONResponse({
            "data": []
        })


@router.get("/push/addDevice.php")
@router.post("/push/addDevice.php")
async def push_add_device(request: Request, device_id: str = None, token: str = None):
    """
    Push notification device registration
    """
    try:
        if request.method == "POST":
            body = await request.json()
            device_id = body.get("device_id", device_id)
            token = body.get("token", token)
    except:
        pass
    
    return JSONResponse({
        "status": "success",
        "device_id": device_id,
        "registered": True
    })


@router.get("/api/")
async def api_root():
    """Root API endpoint"""
    return JSONResponse({
        "status": "online",
        "server": "MuppetsServer",
        "version": "1.0"
    })


@router.get("/")
async def root():
    """Root endpoint"""
    return JSONResponse({
        "status": "online",
        "message": "MuppetsServer is running"
    })
