import React from "react";

function Body() {
    return (
        <main style={Styles.main}>
            <h2>Welcome to my Website</h2>
            <p>This is a simple React application with a structured layout.</p>
        </main>
    );
}

const Styles={
    main: {
        padding:'20px',
        textAlign: 'center',
        backgroundColor: 'pink'
    }
}

export default Body;