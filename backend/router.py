from typing import Annotated
from fastapi  import APIRouter, Body
from fastapi.responses import RedirectResponse

from backend.oauth_google import generate_google_oautn_redirect_uri
from backend.config import settings

import aiohttp

router = APIRouter(prefix='/auth')


@router.get('/google/url')
def get_google_oauth_redirect_url():
    uri = generate_google_oautn_redirect_uri()
    return RedirectResponse(url=uri, status_code=302)


@router.post('/google/callback')
async def handle_code(code: Annotated[str, Body(embed=True)]):
    
    google_token_url = 'https://oauth2.googleapis.com/token'
    
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=google_token_url,
            data={
                'client_id': settings.OUATN,
                'client_secret': settings.GOOGLE_CLIENT_SECRET,
                'code': code,
                'grant_type': 'authorization_code',
                'redirect_uri': 'http://localhost:3000/auth/google'
            }
        ) as response:
            res = await response.json()
            print(f'{res}')
            
    return