import React from "react";
import "./PenPal.css";

const SummarizerView = () => {
  return (
    <div style={{ paddingBottom: "100px" }}>
      <div className="titleContainer">
        <h1
          style={{
            fontWeight: "bold",
            fontFamily: "Roboto",
            padding: 15,
            fontSize: 40,
          }}
        >
          <i style={{ fontFamily: "Victor Mono", fontWeight: "bold" }}>
            PenPal with the Feynman Technique 📝
          </i>{" "}
          <br></br>
          <p style={{ fontSize: 20 }}>
            by <span style={{ color: "#edb51a" }}>Classif</span>
            <span style={{ color: "#1f7ede" }}>.ai</span>
          </p>
        </h1>
      </div>
      <p> </p>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-around",
          flexWrap: "wrap",
        }}
      >
        <div
          style={{
            flex: 1,
            display: "flex",
            flexDirection: "column",
            padding: 30,
          }}
          className="btns-container"
        >
          <div
            style={{
              display: "flex",
              gap: 10,
              justifyContent: "center",
              flexDirection: "column",
            }}
          >
            <div style={{ display: "flex", justifyContent: "space-around" }}>
              <button
                className="btn"
                style={{
                  backgroundColor: "#b3d0ff",
                  color: "#113266",
                  borderRadius: 10,
                }}
              >
                Load MP3 File
              </button>
              <button
                className="btn"
                style={{
                  backgroundColor: "#0388fc",
                  color: "white",
                  borderRadius: 10,
                }}
              >
                <i style={{ fontFamily: "Victor Mono", fontWeight: "bold" }}>
                  PenPal
                </i>{" "}
                My Notes
              </button>
            </div>
          </div>
        </div>
        <div
          style={{
            paddingLeft: 20,
            paddingRight: 20,
            display: "flex",
            padding: 20,
            gap: 10,
          }}
        >
          <textarea
            style={{ backgroundColor: "#082d54", color: "#ededed" }}
            placeholder="Transcript..."
          />
          <textarea
            style={{
              fontStyle: "italic",
              fontWeight: "400",
            }}
            placeholder="PenPal..."
            value={""}
            disabled
          />
        </div>
      </div>
    </div>
  );
};

export default SummarizerView;
