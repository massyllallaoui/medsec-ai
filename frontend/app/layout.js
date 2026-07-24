import './globals.css';

export const metadata = {
  title: 'MedSec AI | Dashboard Clinique',
  description: 'Plateforme B2B d\'analyse médicale sécurisée par IA',
};

export default function RootLayout({ children }) {
  return (
    <html lang="fr">
      <body>{children}</body>
    </html>
  );
}
