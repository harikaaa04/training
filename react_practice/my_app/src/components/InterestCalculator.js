import React, {useState} from "react";

function InterestCalculator() {
    const [principal, setPrincipal] = useState(''); 
    const [rate, setRate] = useState(''); 
    const [time, setTime] = useState(''); 
    const [type, setType] = useState(''); 
    const [result, setResult] = useState(''); 


    const calculateInterest=()=>{
        let P = parseFloat(principal);
        let R = parseFloat(rate);
        let T = parseFloat(time);

        if (isNaN(P) || isNaN(T) || P <= 0 || R <= 0 || T <= 0) {
            setResult("Please enter valid results.");
            return;
        }

        let interest = 0;

        if (type == 'simple') {
            interest = (P*T*R) / 100;
        }
        else {
            interest = P * (Math.pow());
        }
        setResult(`Calculates ${type} interest: ${interest.toFixed(2)}`);
    }
    
    return (
        <div style={styles.container}>
            <h2>Interest Calculator</h2>
            <label>Principal (P);</label>
            <input 
            type = "number"
            value={principal}
            onChange={(e) => setPrincipal(e.target.value)}
            style={styles.input}
            placeholder="Enter Principal Amount"></input>

            <label>Rate of Interest (R);</label>
            <input 
            type = "number"
            value={rate}
            onChange={(e) => setRate(e.target.value)}
            style={styles.input}
            placeholder="Enter Rate"></input>

            <label>Time (T) in Years</label>
            <input 
            type = "number"
            value={time}
            onChange={(e) => setTime(e.target.value)}
            style={styles.input}
            placeholder="Enter Time (years)"></input>

            <label>Select Interest Type</label>
            <select value={type} onChange={(e) => setType(e.target.value)} style={styles.select}>
                <option value="simple">Simple Interest</option>
                <option value="compound">Compound Interest</option>
            </select> 
            
            <button onClick={calculateInterest} style={styles.button}>Calculate</button>
        </div>
    );
}

const styles={
    input:{
        // color: 'pink',
        textAlign: 'center',
        // position: 'fixed',
    }
}

export default InterestCalculator;