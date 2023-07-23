import fastapi as _fastapi
import blockchain as _blockchain

blockchain = _blockchain.Blockchain()
app = _fastapi.FastAPI()

# Endpoint to mine a block
@app.post("/mine_block")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The Blockchain is invalid."
        )
    block = blockchain.mine_block(data=data)

    return block

# Endpoint to get the blockchain
@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The Blockchain is invalid."
        )
    chain = blockchain.chain
    return chain

# Endpoint to validate the blockchain
@app.get("/validate/")
def is_blockchain_valid():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The blockchain is invalid"
        )

    return blockchain.is_chain_valid()

# Endpoint to get the last block of the chain
@app.get("/blockchain/last/")
def previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The blockchain is invalid"
        )

    return blockchain.get_previous_block()
