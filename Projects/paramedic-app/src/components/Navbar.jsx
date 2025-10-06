import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav style={{
      backgroundColor: '#343a40',
      color: '#fff',
      padding: '1rem',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center'
    }}>
      <h1 style={{ margin: 0, fontSize: '1.5rem' }}>🚑 Paramedic Prep</h1>
      <Link to="/" style={{
        color: '#fff',
        textDecoration: 'none',
        fontWeight: 'bold'
      }}>
        Home
      </Link>
       <Link to="/about" style={{ color: "#fff", marginRight: "1rem", textDecoration: "none" }}>About</Link>
        <Link to="/contact" style={{ color: "#fff", textDecoration: "none" }}>Contact</Link>
    </nav>
  );
}

export default Navbar;
