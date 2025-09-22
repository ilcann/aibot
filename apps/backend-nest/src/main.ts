import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';

const serverPort = process.env.NESTJS_PORT || 5000;
const serverUrl = process.env.NESTJS_URL || `http://localhost:5000`;

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  const config = new DocumentBuilder()
    .setTitle('API Documentation')
    .setVersion('1.0')
    .addServer(serverUrl)
    .build();
  const documentFactory = () => SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api', app, documentFactory);

  console.log(`Server running on port ${serverPort}`);
  await app.listen(serverPort);
}
bootstrap();
