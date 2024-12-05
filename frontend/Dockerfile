# Use Node.js as base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN npm install

# Expose port for React
EXPOSE 3000

# Run React app
CMD ["npm", "start"]
