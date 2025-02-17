import React from "react";

function Footer() {
    return (
        <footer style={Styles.footer}>
            <p>&copy; 2024 My Website. All rights reserved.</p>
        </footer>
    )
}

const Styles={
    footer:{
        backgroundColor: '#111',
        color: 'pink',
        textAlign: 'center',
        padding: '11px',
        position: 'fixed',
        width: '100%',
        bottom: 0
    }
}

export default Footer;