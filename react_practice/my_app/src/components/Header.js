import React from 'react';

function Header() {
    return (
        <header style={styles.header}>
            <h1>My Website!</h1>
            <nav>
                <u1 style={styles.navList}>
                <li><a href='#'>Home</a></li>
                    <li><a href='#'>About</a></li>
                    <li><a href='#'>Contacts</a></li>
                </u1>
            </nav>
        </header>
    );
}

const styles = {
    header: {
        backgroundColor: '#111',
        color: 'pink',
        padding: '11px',
        textAlign: 'center'
    },
    navList: {
        listStyleType: 'none',
        padding: 0,
        display:'flex',
        justifyContent: 'center'
    }
}

export default Header;