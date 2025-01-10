use warp::Filter;
use warp::ws::{Message, WebSocket};
use futures::{StreamExt, SinkExt};

#[tokio::main]
async fn main() {
    // creates route filter
    let ws_route = warp::path("ws")
        .and(warp::ws())
        .map(|ws: warp::ws::Ws| {
            ws.on_upgrade(handle_socket)
        });

    println!("WebSocket server running on ws://localhost:8000/ws");

    // runs server
    warp::serve(ws_route).run(([127, 0, 0, 1], 8000)).await;
}

// Handle the WebSocket connection
async fn handle_socket(ws: WebSocket) {
    println!("New WebSocket connection established");

    // transmission, receiver
    let (mut tx, mut rx) = ws.split();

    // on next receiver
    while let Some(result) = rx.next().await {
        match result {
            Ok(msg) => {
                if msg.is_text() {
                    let received_text = msg.to_str().unwrap_or("");
                    println!("Received message: {}", received_text);

                    // transmiss message back
                    // if let Err(e) = tx.send(Message::text(received_text)).await {
                    //     eprintln!("Error sending message: {}", e);
                    //     break;
                    // }
                }
            }
            Err(e) => {
                eprintln!("WebSocket error: {}", e);
                break;
            }
        }
    }

    println!("WebSocket connection closed");
}

/*
TODO:
Player:
    boats -> {"x":2, "y":3, "z":4}
    board -> [
              [x],[x],[y],[o],
              [o],[o],[y],[o],
              [o],[o],[y],[o]
              [z],[z],[z],[z]
            ]

*/
