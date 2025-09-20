# 1. Base image
FROM node:20-alpine

# 2. pnpm kur
RUN npm install -g pnpm

# 3. Çalışma dizini
WORKDIR /app

# 4. package dosyalarını kopyala
COPY package*.json pnpm-lock.yaml ./

# 5. Dependencies yükle
RUN pnpm install

# 6. Kodları kopyala
COPY . .

# 7. Port expose
EXPOSE 3000

# 8. Dev server başlat
CMD ["pnpm", "run", "start:dev"]
