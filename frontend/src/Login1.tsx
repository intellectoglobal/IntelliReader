
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import Sign_in from './assets/Signin.png';
import Google from './assets/Google.png';
import Facebook from './assets/Facebook.png';
import Divider from '@mui/material/Divider';
import AdbIcon from '@mui/icons-material/Adb';
import {  Link } from 'react-router-dom';

const Login1: React.FC = () => {
  return (
    
    <Box sx={{marginTop: 4, display: 'flex', flexDirection: 'column', alignItems: 'center', width: '100%'}} >
      <Typography sx={{ fontFamily:'Outfit',fontWeight: 500, fontSize: '40px', letterSpacing: '0.15px' }}><AdbIcon sx={{display: 'inline', maxHeight: '100%', maxWidth:'100%', marginRight: '5px'}}/>IntelliReader</Typography>
      <Typography sx={{ fontFamily:'Outfit', letterSpacing: 1.25 ,fontWeight: 100, textShadow: '0px 4px 4px rgba(211, 211, 211, 1)' }}>Empower Your PDFs with AI: Simplify. Innovate. Excel.</Typography>
      
      <Grid container spacing={2} sx={{marginTop: 6, maxWidth: '80%', height: 'auto', boxShadow: '4px 4px 8px rgba(0, 0, 0, 0.25)',  borderRadius: '16px' }}>
      <Grid item xs={12} sm={6} p={0} sx={{ backgroundColor: '#CAE8FF', borderRadius: '16px 0 0 16px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <Box
            component="img"
            src={Sign_in}
            alt="Sign in"
            sx={{
              maxWidth: '70%',
            }}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <Box
            sx={{
              
              flexDirection: "column",
              marginLeft: "60px",
              marginRight: "70px",
              marginTop: 0,
              maxWidth: "90%",
              
            }}
          >
            <Typography  mt={0} sx={{ textAlign: "left", fontFamily: "Outfit", fontStyle:"Regular", fontSize:"20px", letterSpacing: '1px' }}>
              Login to IntelliReader
            </Typography>
            <Typography mt={1} sx={{ textAlign: "left", fontFamily: "Outfit", fontStyle: "SemiBold", fontSize:"10px", color: "#6C6363", letterSpacing: '1.25px'}}>
              New User ? <Link to="/signup">Sign Up</Link>
            </Typography>
            <Grid container spacing={1} mt={0} justifyContent={'center'}>
              <Grid item xs={6} >
                <Button variant='outlined' fullWidth
                  sx={{
                    marginTop: '10px',
                    
                    borderColor: 'rgba(0, 0, 0, 0.1)',
                    height: '51px',
                    color: '#6C6363',
                    textTransform: 'none',
                    
                    
                    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.25)',
                    borderRadius: '10px'
                  }}
                >
                  <img src={Google} alt="Google Login" style={{ maxWidth: '30px', marginRight: '20px' }} />
                  <Typography sx={{display: { xs: 'none', sm: 'inline' },fontFamily: 'Outfit',fontSize: '10px', fontWeight: 600, letterSpacing: '1.25px', maxWidth: "100%" }}>Login with Google </Typography>
                </Button>
              </Grid>
              <Grid item xs={6}>
                <Button variant='outlined' fullWidth
                  sx={{
                    marginTop: '10px',
                    height: '51px',
                    borderColor: 'rgba(0, 0, 0, 0.1)',
                    color: '#6C6363',
                    
                    marginLeft: '10px',
                    maxWidth: '100%',
                    textTransform: 'none',
                    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.25)',
                    borderRadius: '10px',
                    
                    
                  }}
                >
                  <img src={Facebook} alt="Facebook Login" style={{ maxWidth: '30px', marginRight: '15px' }} />
                  <Typography sx={{display: { xs: 'none', sm: 'inline' },fontFamily: 'Outfit',fontSize: '10px', fontWeight: 600, letterSpacing: '1.25px', maxWidth: "100%" }}>Login with Facebook</Typography>
                </Button>
              </Grid>
            </Grid>
            <Box sx={{ mt: 0, display: 'flex', justifyContent: 'center', fontSize: '10px', fontWeight: 600, color: '#6C636' }}>
              <Divider sx={{ml: 2,  my: 1, width: '92%', color: '#6C636' }} ><Typography sx={{color:"#6C6363"}}>or</Typography></Divider>
            </Box>
            <Box component="form" noValidate sx={{ mt: 0, my: -2 }}>
              <TextField
              InputProps={{ sx: { borderRadius: '10px' } }}
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email"
                name="email"
                autoComplete="email"
                autoFocus
                sx={{boxShadow: '0 4px 8px rgba(0, 0, 0, 0.25)', borderRadius: '10px'}}
              />
              <TextField
              InputProps={{ sx: { borderRadius: '10px' } }}
                margin="normal"
                required               
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
                sx={{boxShadow: '0 4px 8px rgba(0, 0, 0, 0.25)', borderRadius: '10px'}}
              />
              <Grid container justifyContent="flex-end" mb={0} mt={1}>
                <Grid item>
                  <Link to="#" sx={{fontFamily:'Outfit', fontSize: '13px', letterSpacing: '1.25px', fontStyle: 'Light'}}>
                    Forgot password?
                  </Link>
                </Grid>
                
              </Grid>
              <Button
              
                type="submit"
                fullWidth
                variant="contained"
                
                sx={{ mt: 3, mb: 5, boxShadow: '0 4px 8px rgba(0, 0, 0, 0.25)', borderRadius: '10px', backgroundColor: '#2C346B' }}
              >
                Login
              </Button>
              
            </Box>
          </Box>
        </Grid>
      </Grid>
    </Box>
    
  );
                }
export default Login1;
