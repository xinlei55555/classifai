import React from "react";

const Home = () => {
  return (
    <div>
      <h1
        style={{
          fontWeight: "bold",
          fontFamily: "Roboto",
          padding: 30,
          fontSize: 50,
        }}
      >
        Welcome to <span style={{ color: "#edb51a" }}>ClassIf</span>
        <span style={{ color: "#1f7ede" }}>.ai!</span> 👋
      </h1>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-around",
        }}
      >
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            border: "solid 1px",
          }}
        >
          <div style={{ display: "flex", gap: 10, justifyContent: "center" }}>
            <div>
              <button style={{ backgrounColor: "" }}>Load MP3 File</button>
              <button>Load .txt File</button>
            </div>
          </div>
          <div>
            <button>
              <i>PenPal</i> My Notes
            </button>
          </div>
        </div>
        <div>
          <textarea style={{ border: "solid 1px" }} placeholder="Transcript" />
          <div></div>
          <div>
            <textarea style={{ border: "solid 1px" }} placeholder="PenPal" />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
