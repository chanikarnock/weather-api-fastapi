import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from requests import HTTPError, Response
from src.default_serializer import DefaultResponseSerializer
from src.error_handler_utils import ErrorHandlerUtil
from src.repositories.visual_crossing_repo import VisualCrossingRepo
import redis

rd = redis.Redis(host="localhost", port=6379, db=0)
app = FastAPI()

@app.get("/")
def server_status():
    return {"message": "server status: NORMAL"}


@app.get("/weather")
def get_weather_from_lat_long(request: Request, request_body: dict):
    try:
        result = VisualCrossingRepo().get_weather_from_lat_long(request_body=request_body)
        return DefaultResponseSerializer(data=result)
    except HTTPError as e:
        return Response(status_code=e.response.status_code, content=e.response.content, headers=e.response.headers)
    except Exception as e:
        return ErrorHandlerUtil.handle_error_response(e)
    


@app.get("/weather/us/{zipcode}")
def get_weather_from_us_zipcode(request: Request, zipcode: int):
    try:
        cache = rd.get(zipcode)
        if cache:

            return DefaultResponseSerializer(data=json.loads(cache))
        else:
            result = VisualCrossingRepo().get_weather_from_us_zipcode(zipcode=zipcode)
            dict_str = json.dumps(result)
            rd.set(name=zipcode, value=dict_str, ex=43200)
            return DefaultResponseSerializer(data=result)
    except HTTPError as e:
        return Response(status_code=e.response.status_code, content=e.response.content, headers=e.response.headers)
    
