import type { NextConfig } from 'next';

const isGitHubPages = process.env.GITHUB_ACTIONS === 'true';

const nextConfig: NextConfig = {
  output: 'export',
  trailingSlash: true,
  basePath: isGitHubPages ? '/open-talent-radar' : '',
  assetPrefix: isGitHubPages ? '/open-talent-radar/' : undefined,
};

export default nextConfig;
